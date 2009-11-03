# $Id$
# Authority: dries
# Upstream: Ton Hospel <Heap-Simple$ton,iguana,be>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Heap-Simple

Summary: Heap structures
Name: perl-Heap-Simple
Version: 0.13
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Heap-Simple/

Source: http://www.cpan.org/modules/by-module/Heap/Heap-Simple-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
A heap is a partially sorted structure where it's always easy to extract the
smallest element. If the collection of elements is changing dynamically, a
heap has less overhead than keeping the collection fully sorted.

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
%doc Changes MANIFEST MANIFEST.SKIP META.yml README
%doc %{_mandir}/man3/Heap::Simple.3pm*
%dir %{perl_vendorlib}/Heap/
%{perl_vendorlib}/Heap/Simple/
%{perl_vendorlib}/Heap/Simple.pm

%changelog
* Wed Feb 20 2008 Dag Wieers <dag@wieers.com> - 0.13-1
- Updated to release 0.13.

* Wed Jan 23 2008 Dag Wieers <dag@wieers.com> - 0.12-1
- Updated to release 0.12.

* Fri Dec  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.11-1
- Initial package.
