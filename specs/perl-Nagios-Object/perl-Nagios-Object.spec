# $Id$
# Authority: dag
# Upstream: Albert P Tobey <tobert$gmail,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Nagios-Object

Summary: Nagios::Object - Nagios object configuration parsing
Name: perl-Nagios-Object
Version: 0.20
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Nagios-Object/

Source: http://www.cpan.org/authors/id/T/TO/TOBEYA/Nagios-Object-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 1:5.6.1
BuildRequires: perl(Module::Build)
BuildRequires: perl(Data::Dumper) >= 0.01
BuildRequires: perl(Module::Build) >= 0.26
BuildRequires: perl(Scalar::Util) >= 0.01
BuildRequires: perl(Test::Exception) >= 0.01
BuildRequires: perl(Test::More) >= 0.01
Requires: perl >= 1:5.6.1

%description
Nagios::Object - Nagios object configuration parsing.

%prep
%setup -n %{real_name}-%{version}

%build
#%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
#%{__make} %{?_smp_mflags}
%{__perl} Build.PL
./Build

%install
%{__rm} -rf %{buildroot}
#%{__make} pure_install
PERL_INSTALL_ROOT="%{buildroot}" ./Build install installdirs="vendor"

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog MANIFEST META.yml README
%doc %{_mandir}/man1/config_status_demo.pl.1*
%doc %{_mandir}/man1/parse.pl.1*
%doc %{_mandir}/man1/statusdat_demo.pl.1*
%doc %{_mandir}/man1/test_configuration.pl.1*
%doc %{_mandir}/man3/Nagios::*.3pm*
%{_bindir}/config_status_demo.pl
%{_bindir}/decode_flags.pl
%{_bindir}/parse.pl
%{_bindir}/statusdat_demo.pl
%{_bindir}/test_configuration.pl
%{perl_vendorlib}/Nagios/

%changelog
* Wed Apr 09 2008 Dag Wieers <dag@wieers.com> - 0.20-1
- Initial package. (using DAR)
