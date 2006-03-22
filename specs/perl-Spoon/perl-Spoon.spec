# $Id$
# Authority: dries
# Upstream: Brian Ingerson <ingy$cpan,org>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Spoon

Summary: Spiffy Application Building Framework
Name: perl-Spoon
Version: 0.23
Release: 1.2
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Spoon/

Source: http://search.cpan.org/CPAN/authors/id/I/IN/INGY/Spoon-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Spoon is an Application Framework that is designed primarily for
building Social Software web applications. The Kwiki wiki software is
built on top of Spoon.

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
%{perl_vendorlib}/Spoon.pm
%{perl_vendorlib}/Spoon/

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.23-1.2
- Rebuild for Fedora Core 5.

* Wed Jun  8 2005 Dries Verachtert <dries@ulyssis.org> - 0.23-1
- Updated to release 0.23.

* Fri Mar  4 2005 Dries Verachtert <dries@ulyssis.org> - 0.21-1
- Updated to release 0.21.

* Wed Dec 29 2004 Dries Verachtert <dries@ulyssis.org> - 0.20-1
- Updated to release 0.20.

* Mon Dec 06 2004 Dries Verachtert <dries@ulyssis.org> - 0.18-1
- Initial package.
