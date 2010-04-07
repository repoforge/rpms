# $Id$
# Authority:    hadams

Name:		tango-icon-theme
Version:	0.7.2
Release:	6%{?dist}
Summary:	Icons from Tango Project
Summary(pl):	Ikony Projektu Tango

License:	Creative Commons Attribution Share-Alike
Group:		User Interface/Desktops
URL:		http://tango-freedesktop.org/
Source0:	http://tango-project.org/releases/%{name}-%{version}.tar.gz
BuildArch:	noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires:	icon-naming-utils >= 0.7.2
BuildRequires:	ImageMagick-devel >= 5.5.7
BuildRequires:	librsvg2-devel >= 2.12.3
BuildRequires:	pkgconfig >= 0.19


%description
Contains icons from Tango Project.

%description -l pl
Zawiera ikony Projektu Tango.


%prep
%setup -q


%build
%configure --enable-png-creation
make


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT


%post
touch --no-create %{_datadir}/icons/Tango 2> /dev/null ||:
gtk-update-icon-cache -q %{_datadir}/icons/Tango 2> /dev/null ||:


%postun
touch --no-create %{_datadir}/icons/Tango 2> /dev/null ||:
gtk-update-icon-cache -q %{_datadir}/icons/Tango 2> /dev/null ||:


%files
%defattr(644,root,root,755)
%{_datadir}/icons/Tango
%doc AUTHORS ChangeLog COPYING README 


%changelog
* Thu Sep 27 2007 Heiko Adams <info at fedora-blog dot de> - 0.7.2-6
- version update
- rebuild for rpmforge

* Thu Sep 07 2006 Piotr Drąg <raven at pmail dot pl> - 0.7.2-5
- Added %%{?dist}
- Removed unnecessary automake BuildRequire

* Thu Jul 27 2006 Piotr Drąg <raven at pmail dot pl> - 0.7.2-4
- Drop unnecessary BuildRequires

* Thu Jul 27 2006 Piotr Drąg <raven at pmail dot pl> - 0.7.2-3
- Added --enable-png-creation
- Added librsvg2-devel BuildRequire

* Thu Jul 27 2006 Piotr Drąg <raven at pmail dot pl> - 0.7.2-2
- New scriptlets
- Changed the license name

* Thu Jul 27 2006 Piotr Drąg <raven at pmail dot pl> - 0.7.2-1
- Initial RPM release
