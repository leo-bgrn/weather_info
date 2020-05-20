import unittest
from unittest.mock import patch, Mock

from weather_info.application.forecast import ForecastService
from weather_info.application.forecast.ForecastView import ForecastView
from weather_info.domain.forecast.Forecast import Forecast


class MyTestCase(unittest.TestCase):
    @patch("weather_info.application.forecast.ForecastService.LocationProvider")
    @patch("weather_info.application.forecast.ForecastService.ForecastProvider")
    def test_get_forecast_with_None(self, forecast_provider_mocked, location_provider_mocked):
        location_provider_mocked.get_location.return_value = None
        res = ForecastService.get_forecast("test")

        self.assertIsNone(res)
        location_provider_mocked.get_location.assert_called_once_with("test")
        self.assertFalse(forecast_provider_mocked.get_forecast.called)

    @patch("weather_info.application.forecast.ForecastService.LocationProvider")
    @patch("weather_info.application.forecast.ForecastService.ForecastProvider")
    @patch("weather_info.application.forecast.ForecastService.WindDesignationComputer")
    def test_get_forecast(self, wind_designation_mocked, forecast_provider_mocked, location_provider_mocked):
        location_provider_mocked.get_location.return_value = Mock()
        forecast_provider_mocked.get_forecast.return_value = Forecast(forecast=[Mock(), Mock()],
                                                                      location=Mock())
        wind_designation_mocked.compute_wind_designation.return_value = "wind_designation"
        res: ForecastView = ForecastService.get_forecast("test")

        self.assertEqual("wind_designation", res.forecast[0].wind.designation)
        location_provider_mocked.get_location.assert_called_once_with("test")
        forecast_provider_mocked.get_forecast.assert_called_once_with(
            location_provider_mocked.get_location.return_value)


if __name__ == '__main__':
    unittest.main()
