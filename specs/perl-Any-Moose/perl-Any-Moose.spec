# $Id$
# Authority: cmr
# Upstream: Shawn M Moore <sartak$bestpractical,com>
# Upstream: Florian Ragwitz <rafl$debian,org>
# Upstream: Stevan Little <stevan$iinteractive,com>
# Upstream: Tokuhiro Matsuno <tokuhirom$gmail,com>
# Upstream: Goro Fuji <gfuji$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Any-Moose

Summary: use Moose or Mouse modules
Name: perl-Any-Moose
Version: 0.17
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Any-Moose/

Source: http://www.cpan.org/authors/id/S/SA/SARTAK/Any-Moose-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(Mouse) >= 0.40
BuildRequires: perl >= 5.006_002
Requires: perl(Mouse) >= 0.40
Requires: perl >= 5.006_002

%filter_from_requires /^perl*/d
%filter_setup


%description
use Moose or Mouse modules.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes LICENSE MANIFEST META.yml README
%doc %{_mandir}/man3/Any::Moose.3pm*
%dir %{perl_vendorlib}/Any/
#%{perl_vendorlib}/Any/Moose/
%{perl_vendorlib}/Any/Moose.pm

%changelog
* Mon Dec 05 2011 David Hrbáč <david@hrbac.cz> - 0.17-1
- new upstream release

* Tue Apr 05 2011 Denis Fateyev <denis@fateyev.com> - 0.13-1
- Updated to version 0.13.

* Tue Dec 22 2009 Christoph Maser <cmr@financial.com> - 0.11-1
- Initial package. (using DAR)
