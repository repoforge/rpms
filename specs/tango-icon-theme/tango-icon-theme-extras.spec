# $Id$
# Authority:    hadams

Name:		tango-icon-theme-extras
Version:	0.1.0
Release:	2%{?dist}
Summary:	Extra Icons from the Tango Project

License:	Creative Commons Attribution Share-Alike
Group:		User Interface/Desktops
URL:		http://tango-project.org/

Source0:	http://tango-project.org/releases/%{name}-%{version}.tar.gz
BuildArch:	noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires:	icon-naming-utils >= 0.7.2
BuildRequires:	ImageMagick-devel >= 5.5.7
BuildRequires:	librsvg2-devel >= 2.12.3
BuildRequires:	pkgconfig >= 0.19

Requires:	tango-icon-theme

## Much of this is from the included README file...
%description
Contains extra icons for from the Tango Project. Currently this includes Tango
icons for iPod Digital Audio Player (DAP) devices and the Dell Pocket DJ DAP.


%prep
%setup -q 


%build
%configure --enable-png-creation
make


%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}


%clean
rm -rf %{buildroot}


%post
touch --no-create %{_datadir}/icons/Tango 2> /dev/null ||:
gtk-update-icon-cache -q %{_datadir}/icons/Tango 2> /dev/null ||:


%postun
touch --no-create %{_datadir}/icons/Tango 2> /dev/null ||:
gtk-update-icon-cache -q %{_datadir}/icons/Tango 2> /dev/null ||:


%files
%defattr(-,root,root,-)
%{_datadir}/icons/Tango/*
%doc AUTHORS ChangeLog COPYING README 


%changelog
* Thu Sep 27 2007 Heiko Adams <info at fedora-blog dot de> - 0.1.0-2
- rebuild for rpmforge

* Sat Jan 13 2007 Peter Gordon <peter@thecodergeek.com> - 0.1.0-1
- Initial packaging for Fedora Extras, based heavily on the tango-icon-theme
  spec already in Extras (created by Piotr Drąg).
