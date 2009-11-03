# $Id$
# Authority: dag
# Upstream: Guido Socher <guidosocher$gmail,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Unicode-UTF8simple

Summary: Perl module for conversions to/from UTF8 from/to charactersets
Name: perl-Unicode-UTF8simple
Version: 1.06
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Unicode-UTF8simple/

Source: http://www.cpan.org/modules/by-module/Unicode/Unicode-UTF8simple-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
perl-Unicode-UTF8simple is a Perl module for conversions to/from UTF8
from/to charactersets.

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
%doc MANIFEST META.yml README gb2312.txt
%doc %{_mandir}/man3/Unicode::UTF8simple.3*
%dir %{perl_vendorlib}/Unicode/
%{perl_vendorlib}/Unicode/UTF8simple.pm

%changelog
* Fri May 04 2007 Dag Wieers <dag@wieers.com> - 1.06-1
- Initial package. (using DAR)
