# $Id$
# Authority: dries
# Upstream: Brian Ingerson <ingy$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Spoon

Summary: Spiffy Application Building Framework
Name: perl-Spoon
Version: 0.24
Release: 2%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Spoon/

Source: http://www.cpan.org/authors/id/I/IN/INGY/Spoon-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 5.6.1
BuildRequires: perl(DB_File)
BuildRequires: perl(IO::All) >= 0.32
BuildRequires: perl(Spiffy) >= 0.22
BuildRequires: perl(Template) >= 2.10
BuildRequires: perl(Time::HiRes)
BuildRequires: perl(URI)
BuildRequires: rpm-macros-rpmforge
Requires: perl >= 5.6.1
Requires: perl(DB_File)
Requires: perl(IO::All) >= 0.32
Requires: perl(Spiffy) >= 0.22
Requires: perl(Template) >= 2.10
Requires: perl(Time::HiRes)
Requires: perl(URI)

### remove autoreq Perl dependencies
%filter_from_requires /^perl.*/d
%filter_setup

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
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes META.yml README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Spoon.pm
%{perl_vendorlib}/Spoon/

%changelog
* Thu Feb 24 2011 Steve Huff <shuff@vecna.org> - 0.24-2
- Captured missing dependencies.

* Wed Jan 03 2007 Dries Verachtert <dries@ulyssis.org> - 0.24-1
- Updated to release 0.24.

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
