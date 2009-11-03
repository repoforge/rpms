# $Id$
# Authority: dag
# Upstream: Leon Brocard, C<< <acme$astray,com> >>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Test-Expect

Summary: Automated driving and testing of terminal-based programs
Name: perl-Test-Expect
Version: 0.31
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Test-Expect/

Source: http://www.cpan.org/modules/by-module/Test/Test-Expect-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Module::Build)

%description
Automated driving and testing of terminal-based programs.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}
#%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
#%{__make} %{?_smp_mflags}
%{__perl} Build.PL
./Build

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install
#%{__make} pure_install
PERL_INSTALL_ROOT="%{buildroot}" ./Build install installdirs="vendor"

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGES MANIFEST META.yml README
%doc %{_mandir}/man3/Test::Expect.3pm*
%dir %{perl_vendorlib}/Test/
#%{perl_vendorlib}/Test/Expect/
%{perl_vendorlib}/Test/Expect.pm

%changelog
* Thu May 15 2008 Dag Wieers <dag@wieers.com> - 0.31-1
- Updated to release 0.31.

* Fri May 04 2007 Dag Wieers <dag@wieers.com> - 0.30-1
- Initial package. (using DAR)
