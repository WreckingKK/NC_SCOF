#include "Xmlbuilder.h"

 int main(int argc,char* argv[])
   {
 	std::vector<std::string> filename;
	for(unsigned int i=0; i<(unsigned int)argc;i++ )
		{
		filename.push_back(argv[i]);
		}     
	for (unsigned int i=1;i<filename.size(); i++)
		{
		// Generate a filename with the timestep padded to ten zeros
		string xml_open = filename[i];
		Xmlbuilder build(xml_open.c_str());
		unsigned int N = build.getNumParticles();
		std::vector<unsigned int> type = build.getType();
		std::vector< std::string > typemapping = build.getTypeMapping();
		std::vector<Bond> bonds = build.getBond();
		std::vector< std::string > bondtypemapping = build.getBondTypeMapping();
		
		std::string fname = build.getFilename();
		ifstream from(fname.c_str());
		string::size_type xp = fname.find("xml");
		string outs;
		if (xp!=fname.npos)
			outs = fname.replace(xp,xp+3, "retype.xml");
		else
			outs = fname+".retype.xml";

		ofstream to(outs.c_str());
		if(!from||!to) 
			cout<<" Error!! reading or writing files failed!"<<endl;
		string line;
		bool typeout =false;
		bool bondout =false;
		unsigned int count_type =0;
		unsigned int count_bond =0;		
		while(getline(from, line))
			{
			if(line.find("</type")!= line.npos)
				typeout=false;
			if(line.find("</bond")!= line.npos)
				bondout=false;
				
			if (typeout)
				{
				if(count_type < 512)
					to<<typemapping[type[count_type]]<< "\n";
                else if (512 <= count_type && count_type < 832)
                    to<<typemapping[type[count_type]]+"1"<< "\n";
				else
					to<<typemapping[type[count_type]]+"2"<< "\n";
				count_type += 1;
				}
			else if (bondout)
				{
				Bond bi = bonds[count_bond];
				if(bi.a<=512&&bi.b<=512)
					to<<bondtypemapping[bi.type]<<" "<<bi.a<<" "<<bi.b<< "\n";
				else if (512<bi.a<=832&&512<bi.b<=832)
                    to<<bondtypemapping[bi.type]+"1"<<" "<<bi.a<<" "<<bi.b<< "\n";
                else
					to<<bondtypemapping[bi.type]+"2"<<" "<<bi.a<<" "<<bi.b<< "\n";
				count_bond += 1;
				}
			else
				to<<line<<"\n";

			if(line.find("<type") != line.npos)
				{
				typeout = true;
				}
			if(line.find("<bond") != line.npos)
				{
				bondout=true;
				}
			}
		from.close();
		to.close();			
		}
   }

  

