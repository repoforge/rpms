# $Id$
# Authority: dag
# Upstream: Ed Avis <ed$membled,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Log-TraceMessages

Summary: Perl module named Log-TraceMessages
Name: perl-Log-TraceMessages
Version: 1.4
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Log-TraceMessages/

Source: http://www.cpan.org/modules/by-module/Log/Log-TraceMessages-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
perl-Log-TraceMessages is a Perl module.

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
%doc %{_mandir}/man3/Log::TraceMessages.3pm*
%dir %{perl_vendorlib}/Log/
%{perl_vendorlib}/Log/TraceMessages.pm
%{perl_vendorlib}/auto/Log/TraceMessages/

%changelog
* Fri May 04 2007 Dag Wieers <dag@wieers.com> - 1.4-1
- Initial package. (using DAR)
