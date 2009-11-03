# $Id$
# Authority: dries
# Upstream: Alexis Sukrieh <sukria$sukria,net>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Logger-Syslog

Summary: Wrapper for syslog
Name: perl-Logger-Syslog
Version: 1.1
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Logger-Syslog/

Source: http://www.cpan.org/modules/by-module/Logger/Logger-Syslog-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
A perl wrapper for syslog.

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
%doc CHANGES README
%doc %{_mandir}/man3/Logger::Syslog.3pm*
%dir %{perl_vendorlib}/Logger/
#%{perl_vendorlib}/Logger/Syslog/
%{perl_vendorlib}/Logger/Syslog.pm

%changelog
* Tue Nov 13 2007 Dag Wieers <dag@wieers.com> - 1.1-1
- Updated to release 1.1.

* Sun Nov 19 2006 Dries Verachtert <dries@ulyssis.org> - 1.0-1
- Initial package.
