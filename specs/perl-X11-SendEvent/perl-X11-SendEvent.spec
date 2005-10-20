# $Id$

# Authority: dries
# Upstream: Erick Calder <ecalder$cpan,org>

%define real_name X11-SendEvent
%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)
%define perl_archlib %(eval "`perl -V:archlib`"; echo $archlib)
%define perl_privlib %(eval "`perl -V:privlib`"; echo $privlib)

Summary: Module for sending events to X windows
Name: perl-X11-SendEvent
Version: 1.3
Release: 1
License: MIT
Group: Applications/CPAN
URL: http://search.cpan.org/dist/X11-SendEvent/

Source: http://www.cpan.org/modules/by-module/X11/X11-SendEvent-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
This module presents a simple interface for sending events to
an X window.  It also provides methods for finding windows.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -f %{buildroot}%{perl_archlib}/perllocal.pod
%{__rm} -f %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/X11/SendEvent.pm

%changelog
* Thu Jul 22 2004 Dries Verachtert <dries@ulyssis.org> - 1.3-1
- Initial package.
