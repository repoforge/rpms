# $Id$
# Authority: dries
# Upstream: Stephen McCamant <smcc$csua,berkeley,edu>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name X11-Protocol

Summary: Perl module for the X Window System Protocol
Name: perl-X11-Protocol
Version: 0.54
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/X11-Protocol/

Source: http://www.cpan.org/modules/by-module/X11/X11-Protocol-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
This is a module for the X Window System Protocol.

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
%dir %{perl_vendorlib}/X11/
%{perl_vendorlib}/X11/*.pm
%{perl_vendorlib}/X11/Protocol/

%changelog
* Wed Jun  8 2005 Dries Verachtert <dries@ulyssis.org> - 0.54-1
- Updated to release 0.54.

* Wed Dec 08 2004 Dries Verachtert <dries@ulyssis.org> - 0.53-1
- Initial package.
