

import ScrapePlugins.RunBase
import ScrapePlugins.BtLoader.Run
import ScrapePlugins.BtSeriesFetcher.Run

class Runner(ScrapePlugins.RunBase.ScraperBase):

	loggerPath = "Main.Manga.Bt.Base"
	pluginName = "BtBase"


	def _go(self):
		self.log.info("BtBase calling plugins.")

		self.log.info("BtBase calling Series Monitor.")
		monitor = ScrapePlugins.BtSeriesFetcher.Run.Runner()
		monitor.go()

		self.log.info("BtBase calling Downloader.")


		loader = ScrapePlugins.BtLoader.Run.Runner()
		loader.go()

		self.log.info("BtBase Finished calling plugins.")



if __name__ == "__main__":

	import utilities.testBase as tb

	with tb.testSetup():
		obj = Runner()
		obj.go()


