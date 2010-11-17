# $Id$
# Authority: dries
# Upstream: Adam Kennedy <adamk$cpan,org>

### EL6 ships with perl-CSS-Tiny-1.15-4.el6
%{?el6:# Tag: rfx}

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name CSS-Tiny

Summary: Read and write CSS files
Name: perl-CSS-Tiny
Version: 1.15
Release: 1%{?dist}
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/CSS-Tiny/

Source: http://www.cpan.org/modules/by-module/CSS/CSS-Tiny-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(File::Spec) >= 0.82
BuildRequires: perl(Test::More) >= 0.47

%description
CSS::Tiny is a perl class to read and write .css stylesheets with as
little code as possible, reducing load time and memory overhead. CSS.pm
requires about 2.6 meg or ram to load, which is a large amount of
overhead if you only want to do trivial things. Memory usage is normally
scoffed at in Perl, but in my opinion should be at least kept in mind.

This module is primarily for reading and writing simple files, and
anything we write shouldn't need to have documentation/comments. If you
need something with more power, move up to CSS.pm. With the increasing
complexity of CSS, this is becoming more common, but many situations can
still live with simple CSS files.

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
%doc Changes LICENSE MANIFEST META.yml README
%doc %{_mandir}/man3/CSS::Tiny.3pm*
%dir %{perl_vendorlib}/CSS/
#%{perl_vendorlib}/CSS/Tiny/
%{perl_vendorlib}/CSS/Tiny.pm

%changelog
* Thu Nov 08 2007 Dag Wieers <dag@wieers.com> - 1.15-1
- Updated to release 1.15.

* Mon Sep 18 2006 Dries Verachtert <dries@ulyssis.org> - 1.14-1
- Updated to release 1.14.

* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 1.11-1
- Updated to release 1.11.

* Wed Jun  8 2005 Dries Verachtert <dries@ulyssis.org> - 1.10-1
- Updated to release 1.10.

* Fri Mar  4 2005 Dries Verachtert <dries@ulyssis.org> - 1.08-1
- Updated to release 1.08.

* Thu Jul 22 2004 Dries Verachtert <dries@ulyssis.org> - 1.05-1
- Initial package.
