# $Id$
# Authority: dries
# Upstream: Blair Zajac <blair$orcaware,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Proc-Background

Summary: Generic interface to background process management
Name: perl-Proc-Background
Version: 1.09
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Proc-Background/

Source: http://www.cpan.org/modules/by-module/Proc/Proc-Background-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
This is the Proc::Background package.  It provides a generic interface
to running background processes.  Through this interface, users can
run background processes on different operating systems without
concerning themselves about the specifics of doing this.  Users of
this package create new Proc::Background objects that provide an
object oriented interface to process management.

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
%doc %{_mandir}/man?/*
%{_bindir}/timed-process
%{perl_vendorlib}/Proc/Background.pm
%{perl_vendorlib}/Proc/Background

%changelog
* Fri Jul  3 2009 Christoph Maser <cmr@financial.com> - 1.09-1
- Updated to version 1.09.

* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 1.08-1.2
- Rebuild for Fedora Core 5.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 1.08-1
- Initial package.
