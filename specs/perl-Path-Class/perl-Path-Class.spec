# $Id$
# Authority: dries
# Upstream: Ken Williams <ken$mathforum,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Path-Class

Summary: Cross-platform path specification manipulation
Name: perl-Path-Class
Version: 0.18
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Path-Class/

Source: http://www.cpan.org/authors/id/K/KW/KWILLIAMS/Path-Class-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(Cwd)
BuildRequires: perl(File::Path)
BuildRequires: perl(File::Spec) >= 0.87
BuildRequires: perl(File::Spec::Mac) >= 1.3
BuildRequires: perl(File::Temp)
BuildRequires: perl(File::stat)
BuildRequires: perl(IO::Dir)
BuildRequires: perl(IO::File)
BuildRequires: perl(Test::More)
BuildRequires: perl(overload)
Requires: perl(Cwd)
Requires: perl(File::Path)
Requires: perl(File::Spec) >= 0.87
Requires: perl(File::Spec::Mac) >= 1.3
Requires: perl(File::stat)
Requires: perl(IO::Dir)
Requires: perl(IO::File)
Requires: perl(overload)

%filter_from_requires /^perl*/d
%filter_setup

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
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Path/Class.pm
%{perl_vendorlib}/Path/Class/

%changelog
* Tue Dec 22 2009 Christoph Maser <cmr@financial.com> - 0.18-1
- Updated to version 0.18.

* Sat Jul  4 2009 Christoph Maser <cmr@financial.com> - 0.17-1
- Updated to version 0.17.

* Wed Jan 03 2007 Dries Verachtert <dries@ulyssis.org> - 0.16-1
- Updated to release 0.16.

* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.15-1.2
- Rebuild for Fedora Core 5.

* Sat Jan  7 2006 Dries Verachtert <dries@ulyssis.org> - 0.15-1
- Updated to release 0.15.

* Thu Dec 15 2005 Dries Verachtert <dries@ulyssis.org> - 0.14-1
- Initial package.
