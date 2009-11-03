# $Id$
# Authority: dag
# Upstream: Mark Rogaski <mrogaski$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Log-Agent

Summary: Perl module that implements a logging agent
Name: perl-Log-Agent
Version: 0.307
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Log-Agent/

Source: http://www.cpan.org/modules/by-module/Log/Log-Agent-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Test)

%description
perl-Log-Agent is a Perl module that implements a logging agent.

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
%doc ChangeLog MANIFEST META.yml README
%doc %{_mandir}/man3/*.3pm*
%dir %{perl_vendorlib}/Log/
%{perl_vendorlib}/Log/Agent/
%{perl_vendorlib}/Log/Agent.pm
%dir %{perl_vendorlib}/auto/Log/
%{perl_vendorlib}/auto/Log/Agent/

%changelog
* Sun Aug 19 2007 Dag Wieers <dag@wieers.com> - 0.307-1
- Initial package. (using DAR)
