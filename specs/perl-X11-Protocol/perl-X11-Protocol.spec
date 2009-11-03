# $Id$
# Authority: dries
# Upstream: Stephen McCamant <smcc$csua,berkeley,edu>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name X11-Protocol

Summary: Perl module for the X Window System Protocol
Name: perl-X11-Protocol
Version: 0.56
Release: 1%{?dist}
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/X11-Protocol/

Source: http://www.cpan.org/modules/by-module/X11/X11-Protocol-0.56.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
This is a module for the X Window System Protocol.

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
%doc Changes README
%doc %{_mandir}/man3/*
%dir %{perl_vendorlib}/X11/
%{perl_vendorlib}/X11/*.pm
%{perl_vendorlib}/X11/Protocol/

%changelog
* Tue Nov 14 2006 Dries Verachtert <dries@ulyssis.org> - 0.56-1
- Updated to release 0.56.

* Sun Mar 26 2006 Dries Verachtert <dries@ulyssis.org> - 0.55-1
- Updated to release 0.55.

* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.54-1.2
- Rebuild for Fedora Core 5.

* Wed Jun  8 2005 Dries Verachtert <dries@ulyssis.org> - 0.54-1
- Updated to release 0.54.

* Wed Dec 08 2004 Dries Verachtert <dries@ulyssis.org> - 0.53-1
- Initial package.
