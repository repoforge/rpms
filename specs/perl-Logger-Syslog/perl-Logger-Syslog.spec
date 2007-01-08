# $Id$
# Authority: dries
# Upstream: Alexis Sukrieh <sukria+perl$sukria,net>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Logger-Syslog

Summary: Wrapper for syslog
Name: perl-Logger-Syslog
Version: 1.0
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Logger-Syslog/

Source: http://search.cpan.org//CPAN/authors/id/S/SU/SUKRIA/Logger-Syslog-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
A perl wrapper for syslog.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README
%doc %{_mandir}/man3/Logger::Syslog*
%{perl_vendorlib}/Logger/Syslog.pm

%changelog
* Sun Nov 19 2006 Dries Verachtert <dries@ulyssis.org> - 1.0-1
- Initial package.
