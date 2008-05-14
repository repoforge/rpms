# $Id$
# Authority: dag
# Upstream: Sullivan Beck <sbeck$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Date-Manip

Summary: Perl module that provides date manipulation routines
Name: perl-Date-Manip
Version: 5.54
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Date-Manip/

Source: http://www.cpan.org/modules/by-module/Date/Date-Manip-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 0:5.6.0
BuildRequires: perl(Test::More)
Requires: perl >= 0:5.6.0

%description
perl-Date-Manip is a Perl module that provides date manipulation routines.

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

### Clean up docs
find examples/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc HISTORY INSTALL LICENSE MANIFEST META.yml README README.FIRST TODO examples/
%doc %{_mandir}/man3/Date::Manip.3pm*
%dir %{perl_vendorlib}/Date/
#%{perl_vendorlib}/Date/Manip/
%{perl_vendorlib}/Date/Manip.pm
%{perl_vendorlib}/Date/Manip.pod

%changelog
* Tue Dec 04 2007 Dag Wieers <dag@wieers.com> - 5.48-1
- Updated to release 5.48.

* Sun Oct 07 2007 Dag Wieers <dag@wieers.com> - 5.46-1
- Initial package. (using DAR)
