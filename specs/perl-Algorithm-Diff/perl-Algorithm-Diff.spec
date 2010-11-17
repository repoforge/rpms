# $Id$
# Authority: dries
# Upstream: Tye McQueen <tyemq$cpan,org>

### EL6 ships with perl-Algorithm-Diff-1.1902-9.el6
%{?el6:# Tag: rfx}

%define real_name Algorithm-Diff
%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

Summary: Compute intelligent differences between two files or lists
Name: perl-Algorithm-Diff
Version: 1.1902
Release: 1%{?dist}
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Algorithm-Diff/

Source: http://www.cpan.org/modules/by-module/Algorithm/Algorithm-Diff-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
This is a module for computing the difference between two files, two
strings, or any other two lists of things.  It uses an intelligent
algorithm similar to (or identical to) the one used by the Unix "diff"
program.  It is guaranteed to find the *smallest possible* set of
differences.

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
%{perl_vendorlib}/Algorithm/

%changelog
* Tue Sep 19 2006 Dries Verachtert <dries@ulyssis.org> - 1.1902-1
- Updated to release 1.1902.

* Fri Jan  7 2005 Dries Verachtert <dries@ulyssis.org> - 1.1901-1
- Initial package.
