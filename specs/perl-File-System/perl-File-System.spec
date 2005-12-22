# $Id$
# Authority: dries
# Upstream: Andrew Sterling Hanenkamp <sterling$hanenkamp,com>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name File-System

Summary: Provides a general framework for access to a hierarchical data structure
Name: perl-File-System
Version: 1.16
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/File-System/

Source: http://search.cpan.org/CPAN/authors/id/H/HA/HANENKAMP/File-System-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

#BuildArch: noarch
BuildRequires: perl

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
%{__perl} Makefile.PL INSTALLDIRS="vendor" destdir="%{buildroot}"
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
%{perl_vendorlib}/File/System.pm
%{perl_vendorlib}/File/System/

%changelog
* Fri Dec  9 2005 Dries Verachtert <dries@ulyssis.org> - 1.16-1
- Initial package.
