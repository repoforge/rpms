# $Id$
# Authority: dries
# Upstream: Barrie Slaymaker <barries$slaysys,com>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name IPC-Run3

Summary: Run a subprocess in batch mode
Name: perl-IPC-Run3
Version: 0.034
Release: 1.2
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/IPC-Run3/

Source: http://www.cpan.org/modules/by-module/IPC/IPC-Run3-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Run a subprocess in batch mode.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

### Clean up buildroot
%{__rm} -rf %{buildroot}%{perl_archlib} \
		%{buildroot}%{perl_vendorarch}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README Changes
%doc %{_mandir}/man3/*
%dir %{perl_vendorlib}/IPC/
%{perl_vendorlib}/IPC/Run3.pm
%{perl_vendorlib}/IPC/Run3/

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.034-1.2
- Rebuild for Fedora Core 5.

* Sat Jan  7 2006 Dries Verachtert <dries@ulyssis.org> - 0.034-1
- Updated to release 0.034.

* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 0.032-1
- Updated to release 0.032.

* Fri Dec 10 2004 Dries Verachtert <dries@ulyssis.org> - 0.01-1
- Initial package.
