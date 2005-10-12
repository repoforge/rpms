# $Id$
# Authority: dries
# Upstream: Earl Hood <ehood$cpan,org>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Proc-Daemon

Summary: Run a perl program as a daemon process
Name: perl-Proc-Daemon
Version: 0.03
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Proc-Daemon/

Source: http://www.cpan.org/modules/by-module/Proc/Proc-Daemon-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Proc::Daemon provides the capability for a Perl program to run
as a Unix daemon process.

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
%doc Changes README
%doc %{_mandir}/man3/*
%dir %{perl_vendorlib}/Proc/
%{perl_vendorlib}/Proc/Daemon.pm

%changelog
* Mon Dec 06 2004 Dries Verachtert <dries@ulyssis.org> - 0.03-1
- Initial package.
