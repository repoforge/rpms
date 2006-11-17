# $Id$
# Authority: dries
# Upstream: Jos Boumans <gro,miwd$enak>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name IPC-Cmd

Summary: Finding and running system commands made easy
Name: perl-IPC-Cmd
Version: 0.34
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/IPC-Cmd/

Source: http://www.cpan.org/modules/by-module/IPC/IPC-Cmd-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Allows for the searching and execution of any binary on your system.
It adheres to verbosity settings and is able to run intereactive. It
also has an option to capture output/error buffers.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -rf %{buildroot}%{perl_archlib} %{buildroot}%{perl_vendorarch}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README
%doc %{_mandir}/man3/*
%dir %{perl_vendorlib}/IPC/
%{perl_vendorlib}/IPC/Cmd.pm

%changelog
* Tue Nov 14 2006 Dries Verachtert <dries@ulyssis.org> - 0.34-1
- Updated to release 0.34.

* Mon Sep 18 2006 Dries Verachtert <dries@ulyssis.org> - 0.25-1
- Updated to release 0.25.

* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.24-1.2
- Rebuild for Fedora Core 5.

* Thu Mar 31 2005 Dries Verachtert <dries@ulyssis.org> - 0.24-1
- Initial package.

