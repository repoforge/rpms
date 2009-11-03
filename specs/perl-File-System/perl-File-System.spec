# $Id$
# Authority: dries
# Upstream: Andrew Sterling Hanenkamp <sterling$hanenkamp,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name File-System

Summary: Provides a general framework for access to a hierarchical data structure
Name: perl-File-System
Version: 1.16
Release: 2%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/File-System/

Source: http://www.cpan.org/modules/by-module/File/File-System-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

#BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(Module::Build)
BuildRequires: perl(Parse::RecDescent)

%description
The goal of the File::System module is to provide a very general framework for
providing access to a heirarchical data structure. Each member of this data
structure has a set of properties and is marked as containing "content" and/or
as a "container". Something that only provides content is analogous to a file.
Something that only contains other things is analogous to a directory. However,
this framework doesn't exclude the possibility that a thing could have the
features of both.

These features are important if one wishes to make a non-filesystem interface
appear as such. For example, this system allows for the possibility of an
LDAP-accessible database or RDBMS being used as if they were file systems. This
might seem a little senseless at first, but if we wish to provide a system for
mapping a VFS like this to URLs for web or other purposes, it begins to make
more sense.

%prep
%setup -n %{real_name}-%{version}

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

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
%doc %{_mandir}/man3/*.3pm*
%dir %{perl_vendorlib}/File/
%{perl_vendorlib}/File/System.pm
%{perl_vendorlib}/File/System/

%changelog
* Fri Jun 09 2006 Dag Wieers <dag@wieers.com> - 1.16-2
- Added perl(Parse::RecDescent) dependency. (Silviu Mocanu)

* Fri Dec  9 2005 Dries Verachtert <dries@ulyssis.org> - 1.16-1
- Initial package.
