%define name	disc-cover
%define version 1.5.6
%define release %mkrel 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Makes covers for audio CDs using CDDB info
License:	GPL
Group:		Graphics
Source:		http://www.vanhemert.co.uk/files/%{name}-%{version}.tar.bz2
URL:		http://www.vanhemert.co.uk/disc-cover.html
Requires:	tetex-dvips
Requires:	tetex-latex
Requires:	perl-Audio-CD
BuildArch:	noarch

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

