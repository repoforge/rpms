# $Id$
# Authority: dries

# Screenshot: http://kombat.kajaani.net/ss/07.png

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
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++, SDL-devel, SDL_ttf-devel, SDL_net-devel

%description
todo

%prep
%setup -n kajaani_kombat_v%{version}

%build
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%files
%defattr(-, root, root, 0755)

%changelog
* Fri Feb 27 2004 Dries Verachtert <dries@ulyssis.org> 0.3-1
- first packaging for Fedora Core 1
