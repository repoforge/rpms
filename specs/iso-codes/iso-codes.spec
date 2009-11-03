# $Id$
# Authority: dag

Summary: ISO code lists and translations
Name: iso-codes
Version: 1.0a
Release: 1%{?dist}
License: LGPL
Group: System Environment/Base
URL: http://alioth.debian.org/projects/pkg-isocodes/

Source:	http://ftp.debian.org/debian/pool/main/i/iso-codes/iso-codes_%{version}.orig.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: gettext

%description
This package provides the ISO-639 Language code list, the ISO-3166 
Territory code list, and ISO-3166-2 sub-territory lists, and all their 
translations in gettext .po form.

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup

%build
%configure
%{__make}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"
%find_lang iso_639
%find_lang iso_639_3
%find_lang iso_3166_2
%find_lang iso_3166
%find_lang iso_4217
%{__cat} *.lang >%{name}.lang

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc ChangeLog LGPL-2.1 README
%{_datadir}/iso-codes/
%dir %{_datadir}/xml/
%{_datadir}/xml/iso-codes/

%files devel
%defattr(-, root, root, 0755)
%{_datadir}/pkgconfig/iso-codes.pc

%changelog
* Mon Jun 25 2007 Dag Wieers <dag@wieers.com> - 1.0a-1
- Initial package. (using DAR)
