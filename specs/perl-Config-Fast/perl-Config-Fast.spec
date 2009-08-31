# $Id: perl-Config-Any.spec 7464 2009-07-15 13:43:54Z shuff $
# Authority: shuff
# Upstream: Nate Wiger <nwiger$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Config-Fast

Summary: Extremely fast configuration file parser
Name: perl-Config-Fast
Version: 1.07
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Config-Fast/

Source: http://www.cpan.org/modules/by-module/Config/Config-Fast-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 0:5.6.0
#BuildRequires: perl(Test::More)
Requires: perl >= 0:5.6.0

%description
This module is designed to provide an extremely lightweight way to parse
moderately complex configuration files. As such, it exports a single
function - fastconfig() - and does not provide any OO access methods.
Still, it is fairly full-featured.

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
%doc Changes MANIFEST README
%doc %{_mandir}/man3/Config::Fast.3pm*
%dir %{perl_vendorlib}/Config/
%{perl_vendorlib}/Config/Fast.pm

%changelog
* Wed Aug 26 2009 Steve Huff <shuff@vecna.org> - 1.07-1
- Initial package.
