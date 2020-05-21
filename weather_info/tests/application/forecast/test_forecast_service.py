import unittest
from datetime import date
from unittest.mock import patch, Mock

from weather_info.application.forecast import ForecastService
from weather_info.application.forecast.ForecastView import ForecastView
from weather_info.domain.forecast.Forecast import Forecast
from weather_info.domain.pollution.Pollution import Pollution


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
    @patch("weather_info.application.forecast.ForecastService.PollutionProvider")
    def test_get_forecast(self, pollution_provider_mocked, wind_designation_mocked, forecast_provider_mocked,
                          location_provider_mocked):
        location_provider_mocked.get_location.return_value = Mock()
        forecast_provider_mocked.get_forecast.return_value = Forecast(forecast=[Mock(), Mock()],
                                                                      location=Mock())
        forecast_provider_mocked.get_forecast.return_value.forecast[0].value_date = date(2020, 5, 21)
        forecast_provider_mocked.get_forecast.return_value.forecast[1].value_date = date(2020, 5, 22)
        wind_designation_mocked.compute_wind_designation.return_value = "wind_designation"
        pollution_provider_mocked.get_pollution.return_value = Pollution(date(2020, 5, 21), Mock(), 10)
        res: ForecastView = ForecastService.get_forecast("test")

        self.assertEqual("wind_designation", res.forecast[0].wind.designation)
        location_provider_mocked.get_location.assert_called_once_with("test")
        forecast_provider_mocked.get_forecast.assert_called_once_with(
            location_provider_mocked.get_location.return_value)
        self.assertIsNotNone(res.forecast[0].pollution)


if __name__ == '__main__':
    unittest.main()
