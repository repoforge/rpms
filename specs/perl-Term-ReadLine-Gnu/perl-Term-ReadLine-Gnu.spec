# $Id: $

# Authority: dries
# Upstream:

%define real_name Term-ReadLine-Gnu
%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)
%define perl_archlib %(eval "`perl -V:archlib`"; echo $archlib)
%define perl_privlib %(eval "`perl -V:privlib`"; echo $privlib)

# todo mv dir, wrong name

Summary: Extension for the GNU Readline/History library
Name: perl-Term-ReadLine-Gnu
Version: 1.14
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Term-ReadLine-Gnu/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://search.cpan.org/CPAN/authors/id/H/HA/HAYASHI/Term-ReadLine-Gnu-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl, readline-devel

%description
Term::ReadLine::Gnu (TRG) is an implementation of the
interface to the GNU Readline Library.  This module gives you
input line editing facility, input history management
facility, word completion facility, etc.  It uses the real GNU
Readline Library and has the interface with the almost all
variables and functions which are documented in the GNU
Readline/History Library.  So you can program your custom
editing function, your custom completion function, and so on
with Perl.  TRG may be useful for a C programmer to prototype
a program which uses the GNU Readline Library.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" destdir=%{buildroot}
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__sed} -i "s/\/usr\/local\/bin\/perl/\/usr\/bin\/perl/g;" %{buildroot}%{perl_vendorarch}/Term/ReadLine/Gnu/*.pm

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README
%{_mandir}/man3/*
%exclude %{_libdir}/perl5/*/i386-linux-thread-multi/perllocal.pod
%{perl_vendorarch}/Term/ReadLine/Gnu*
%{perl_vendorarch}/auto/Term/ReadLine/Gnu/*
%exclude %{perl_vendorarch}/auto/*/*/*/.packlist

%changelog
* Wed Jun 16 2004 Dries Verachtert <dries@ulyssis.org> - 1.14-1
- Initial package.
