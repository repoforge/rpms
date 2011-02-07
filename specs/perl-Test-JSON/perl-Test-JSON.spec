# $Id$
# Upstream: Curtis 'Ovid' Poe <ovid@cpan.org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)
%define real_name Test-JSON

Summary: Test JSON data
Name: perl-Test-JSON
Version: 0.11
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Test-JSON/

Source: http://search.cpan.org/CPAN/authors/id/O/OV/OVID/Test-JSON-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

BuildRequires: perl(JSON::Any) >= 1.2
BuildRequires: perl(Test::Differences) >= 0.47
BuildRequires: perl(Test::Simple) >= 0.62
BuildRequires: perl(Test::Tester) >= 0.107
Requires: perl(JSON::Any) >= 1.2
Requires: perl(Test::Differences) >= 0.47
Requires: perl(Test::Simple) >= 0.62
Requires: perl(Test::Tester) >= 0.107

### remove autoreq Perl dependencies
%filter_from_requires /^perl.*/d
%filter_setup


%description


%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST META.yml README
%doc %{_mandir}/man3/Test::JSON.3pm*
%dir %{perl_vendorlib}/
%{perl_vendorlib}/Test/JSON.pm
%exclude %{perl_vendorarch}/auto/*/*/.packlist

%changelog
* Mon Feb 07 2011 Christoph Maser <cmaser.gmx.de> - 0.11-1
- initial package
