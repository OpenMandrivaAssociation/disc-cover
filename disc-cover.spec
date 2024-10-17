%define name	disc-cover
%define version 1.5.6
%define release 6

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Makes covers for audio CDs using CDDB info
License:	GPL
Group:		Graphics
Source:		http://www.vanhemert.co.uk/files/%{name}-%{version}.tar.bz2
URL:		https://www.vanhemert.co.uk/disc-cover.html
Requires:	tetex-dvips
Requires:	tetex-latex
Requires:	perl-Audio-CD
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
Provides an easy way to produce covers for audio cds.  It scans audio CDs and
uses information from the CDDB database to build a back and front cover for the
CD.  The cover output is in Latex, Dvi, Pdf or Postscript.  This little gadget
lets you produce covers without typing in all the information yourself.  An
easy way to replace all those lost covers ;-)

%prep
%setup -q

%build

%install
rm -rf %{buildroot}
install -d -m 755 %{buildroot}%{_bindir}
install -d -m 755 %{buildroot}%{_datadir}/%{name}
install -m 0755 disc-cover %{buildroot}%{_bindir}
chmod 755 templates
chmod 644 templates/*
cp -r templates %{buildroot}%{_datadir}/%{name}
#fix doc permissions
chmod 644 AUTHORS COPYING CHANGELOG TODO

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS COPYING CHANGELOG TODO
%{_bindir}/disc-cover
%_datadir/disc-cover/



%changelog
* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 1.5.6-5mdv2011.0
+ Revision: 617786
- the mass rebuild of 2010.0 packages

* Thu Sep 03 2009 Thierry Vignaud <tv@mandriva.org> 1.5.6-4mdv2010.0
+ Revision: 428277
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 1.5.6-3mdv2009.0
+ Revision: 244338
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 1.5.6-1mdv2008.1
+ Revision: 123976
- kill re-definition of %%buildroot on Pixel's request
- import disc-cover


* Fri Jun 30 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.5.6-1mdv2007.0
- New version 1.5.6
- spec cleanup

* Mon Jun 19 2006 Götz Waschk <waschk@mandriva.org> 1.5.5-1mdv2007.0
- drop patch
- new URL
- new version

* Fri Jun 24 2005 Götz Waschk <waschk@mandriva.org> 1.5.4-4mdk
- replace the now missing isolatin1 package

* Sun Dec 19 2004 Guillaume Rousse <guillomovitch@mandrake.org> 1.5.4-3mdk 
- fix URL (close #12724)

* Sun Dec 12 2004 Guillaume Rousse <guillomovitch@mandrake.org> 1.5.4-2mdk
- Rebuild

* Fri Nov 28 2003 Guillaume Rousse <guillomovitch@mandrake.org> 1.5.4-1mdk
- new version

* Sun Nov 09 2003 Guillaume Rousse <guillomovitch@linux-mandrake.com> 1.5.3-1mdk
- new version

* Tue Jul 08 2003 Guillaume Rousse <guillomovitch@linux-mandrake.com> 1.5.2-2mdk
- new URL

* Fri Jun 27 2003 Lenny Cartier <lenny@mandrakesoft.com> 1.5.2-1mdk
- 1.5.2

* Wed Mar 19 2003 Götz Waschk <waschk@linux-mandrake.com> 1.5.0-2mdk
- add the missing templates

* Tue Mar 18 2003 Guillaume Rousse <g.rousse@linux-mandrake.com> 1.5.0-1mdk
- 1.5.0

* Tue Jan 28 2003 Lenny Cartier <lenny@mandrakesoft.com> 1.4.0-2mdk
- rebuild

* Sun Dec 08 2002 Guillaume Rousse <g.rousse@linux-mandrake.com> 1.4.0-1mdk
- 1.4.0

* Tue Oct 15 2002 Lenny Cartier <lenny@mandrakesoft.com> 1.3.2-1mdk
- 1.3.2

* Thu Jan 31 2002 Lenny Cartier <lenny@mandrakesoft.com> 1.3.1-1mdk
- 1.3.1

* Tue Jan 15 2002 Götz Waschk <waschk@linux-mandrake.com> 1.3.0-2mdk
- requires perl-Audio-CD instead of Audio-CD

* Mon Jan 14 2002 Guillaume Rousse <g.rousse@linux-mandrake.com> 1.3.0-1mdk
- 1.3.0

* Mon Sep 10 2001 Lenny Cartier <lenny@mandrakesoft.com> 1.2.2-3mdk
- fixes from Götz Waschk <waschk@linux-mandrake.com>:
	- fix permissions of doc files

* Wed Sep 05 2001 Lenny Cartier <lenny@mandrakesoft.com> 1.2.2-2mdk
- rebuild

* Wed Jul 18 2001 Lenny Cartier <lenny@mandrakesoft.com> 1.2.2-1mdk
- updated by Guillaume Rousse <g.rousse@linux-mandrake.com> :
	- update to 1.2.2

* Mon Jul 02 2001 Lenny Cartier <lenny@mandrakesoft.com> 1.2.1-1mdk
- update to 1.2.1

* Mon Feb 12 2001 Lenny Cartier <lenny@mandrakesoft.com> 1.2.0-1mdk
- updated by Guillaume Rousse <g.rousse@mandrake-linux.com> :
	- cleaned spec
	- upgraded to 1.2.0

* Mon Jan 15 2001 Lenny Cartier <lenny@mandrakesoft.com> 1.1.1-1mdk
- used srpm from Guillaume Rousse <g.rousse@linux-mandrake.com> :
	- upgraded to 1.1.1
	- removed config file

* Sat Dec 16 2000 Guillaume Rousse <g.rousse@linux-mandrake.com> 1.1.0-1mdk
- upgraded to 1.1.0
- commented unecessary CVS file removing
- added TODO file in doc
- used noreplace for config file

* Fri Oct 18 2000 Lenny Cartier <lenny@mandrakesoft.com> 1.0.1-1mdk
- used srpm from Jan Dittberner <jan@jan-dittberner.de> :
	first Mandrake package
- delete CVS system files
