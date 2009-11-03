# $Id$
# Authority: dries
# Upstream: Alan K, Stebbens <aks$software,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Data-ShowTable

Summary: Format data in columns
Name: perl-Data-ShowTable
Version: 3.3
Release: 1.2%{?dist}
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Data-ShowTable/

Source: http://www.cpan.org/modules/by-module/Data/Data-ShowTable-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
This is a Perl 5 module which defines subroutines
to print arrays of data in a nicely formatted listing, using one of
four possible formats: simple table, boxed table, list style, and
HTML-formatting (for World-Wide-Web output).

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install
%{__rm} -f %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist
%{__rm} -f %{buildroot}%{perl_archlib}/perllocal.pod
%{__sed} -i "s/\/usr\/bin\/perl5/\/usr\/bin\/perl/g;" %{buildroot}%{_bindir}/showtable

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes GNU-LICENSE README
%{_bindir}/showtable
%{_mandir}/man?/*
%{perl_vendorlib}/Data/ShowTable.pm

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 3.3-1.2
- Rebuild for Fedora Core 5.

* Wed Jun 16 2004 Dries Verachtert <dries@ulyssis.org> - 3.3-1
- Initial package.
