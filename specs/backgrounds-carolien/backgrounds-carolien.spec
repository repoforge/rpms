# $Id$
# Authority: dries
# Upstream: Carolien Coenen <carolien$ulyssis,org>

Summary: carolien-backgrounds-v1.0.zip
Name: backgrounds-carolien
Version: 1.0
Release: 1%{?dist}
License: creative commons (by-nc-nd/2.0/be)
Group: Applications/Multimedia
URL: http://carolien.ulyssis.org/

Source: http://carolien.ulyssis.org/carolien-backgrounds-v%{version}.zip
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

Buildarch: noarch

%description
Some foto's made by Carolien Coenen which can be used as backgrounds.

%prep
%setup -n backgrounds

%build

%install
%{__rm} -rf %{buildroot}
%{__mkdir_p} %{buildroot}%{_datadir}/backgrounds/images/carolien/
%{__install} *.JPG %{buildroot}%{_datadir}/backgrounds/images/carolien/

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%{_datadir}/backgrounds/images/carolien/

%changelog
* Sat May 06 2006 Dries Verachtert <dries@ulyssis.org> - 1.0-1
- Initial package.
