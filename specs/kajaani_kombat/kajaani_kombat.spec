# $Id$

# Authority: dries

Summary: todo
Name: kajaani_kombat
Version: 0.3
Release: 1
License: todo
Group: Amusements/Games
URL: http://kombat.kajaani.net/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://kombat.kajaani.net/dl/kajaani_kombat_v%{version}.tar.gz
BuildRoot: %{_tmppath}/root-%{name}-%{version}
BuildRequires: SDL

# Screenshot: http://kombat.kajaani.net/ss/07.png

%description
todo

%prep
%{__rm} -rf "${RPM_BUILD_ROOT}"
%setup -n kajaani_kombat_v%{version}

%build
%{__make} %{?_smp_mflags}

%install
#mkdir -p %{
%makeinstall

%files
%defattr(-,root,root, 0755)

%changelog
* Fri Feb 27 2004 Dries Verachtert <dries@ulyssis.org> 0.3-1
- first packaging for Fedora Core 1
