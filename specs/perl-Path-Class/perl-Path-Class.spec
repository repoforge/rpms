# $Id$
# Authority: dries
# Upstream: Ken Williams <ken$mathforum,org>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Path-Class

Summary: Cross-platform path specification manipulation
Name: perl-Path-Class
Version: 0.16
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Path-Class/

Source: http://search.cpan.org/CPAN/authors/id/K/KW/KWILLIAMS/Path-Class-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
'Path::Class' is a module for manipulation of file and directory
specifications (strings describing their locations, like
`'/home/ken/foo.txt'' or `'C:\Windows\Foo.txt'') in a cross-platform
manner. It supports pretty much every platform Perl runs on, including
Unix, Windows, Mac, VMS, Epoc, Cygwin, OS/2, and NetWare.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Path/Class.pm
%{perl_vendorlib}/Path/Class/

%changelog
* Wed Jan 03 2007 Dries Verachtert <dries@ulyssis.org> - 0.16-1
- Updated to release 0.16.

* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.15-1.2
- Rebuild for Fedora Core 5.

* Sat Jan  7 2006 Dries Verachtert <dries@ulyssis.org> - 0.15-1
- Updated to release 0.15.

* Thu Dec 15 2005 Dries Verachtert <dries@ulyssis.org> - 0.14-1
- Initial package.
