# $Id$
# Authority: dries
# Upstream: Randy J Ray <rjray$blackperl,com>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Devel-Modlist

Summary: Collect module use information
Name: perl-Devel-Modlist
Version: 0.6
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Devel-Modlist/

Source: http://search.cpan.org/CPAN/authors/id/R/RJ/RJRAY/Devel-Modlist-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl, perl(ExtUtils::MakeMaker)

%description
Devel::Modlist is a small tool that emits a list of files that were brought
into a script via 'require' or 'use'. It lists these to the STDOUT descriptor
at the end of the script's run. Each file is converted to class-like name,
e.g. IO/File.pm is displayed as IO::File, and the version number, if found,
is displayed. Files ending in .al (auto-loading routines) and .ix (indices
for auto-loading) are ignored. Optionally, one can request that files in
the Perl core library area not be listed (see the manual page).

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Devel/Modlist.pm

%changelog
* Fri Jun  2 2006 Dries Verachtert <dries@ulyssis.org> - 0.6-1
- Updated to release 0.6.

* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.5-1.2
- Rebuild for Fedora Core 5.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.5-1
- Initial package.
