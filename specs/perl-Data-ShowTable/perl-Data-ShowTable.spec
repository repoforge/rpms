# $Id: $

# Authority: dries
# Upstream:

%define real_name Data-ShowTable
%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)
%define perl_archlib %(eval "`perl -V:archlib`"; echo $archlib)
%define perl_privlib %(eval "`perl -V:privlib`"; echo $privlib)

Summary: Format data in columns 
Name: perl-Data-ShowTable
Version: 3.3
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Data-ShowTable/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://search.cpan.org/CPAN/authors/id/A/AK/AKSTE/Data-ShowTable-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl

%description
This is a Perl 5 module which defines subroutines
to print arrays of data in a nicely formatted listing, using one of
four possible formats: simple table, boxed table, list style, and
HTML-formatting (for World-Wide-Web output).

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" destdir=%{buildroot}
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__sed} -i "s/\/usr\/bin\/perl5/\/usr\/bin\/perl/g;" %{buildroot}%{_bindir}/showtable

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README Changes GNU-LICENSE
%{_bindir}/showtable
%{_mandir}/man?/*
%{perl_vendorlib}/Data/ShowTable.pm
%{perl_archlib}/perllocal.pod
%exclude %{perl_vendorarch}/auto/*/*/.packlist

%changelog
* Wed Jun 16 2004 Dries Verachtert <dries@ulyssis.org> - 3.3-1
- Initial package.
