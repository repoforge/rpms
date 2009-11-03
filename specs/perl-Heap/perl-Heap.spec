# $Id$
# Authority: dries
# Upstream: John Macdonald <john$perlwolf,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Heap

Summary: Perl extensions for keeping data partially sorted
Name: perl-Heap
Version: 0.80
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Heap/

Source: http://www.cpan.org/modules/by-module/Heap/Heap-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
This is a collection of routines for managing a heap data structure. There are
two major components: a heap component, and an element component. A heap
package basically keeps a collection of elements and is able to return the
smallest one. The heap component interface is defined in Heap(3) and must be
supported by all heap packages.

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
%doc Changes MANIFEST META.yml README TODO
%doc %{_mandir}/man3/Heap.3pm*
%doc %{_mandir}/man3/Heap::*.3pm*
%{perl_vendorlib}/Heap/
%{perl_vendorlib}/Heap.pm

%changelog
* Fri Nov 09 2007 Dag Wieers <dag@wieers.com> - 0.80-1
- Updated to release 0.80.

* Mon Dec 06 2004 Dries Verachtert <dries@ulyssis.org> - 0.71-1
- Initial package.
