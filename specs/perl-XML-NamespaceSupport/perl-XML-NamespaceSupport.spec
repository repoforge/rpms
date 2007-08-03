# $Id$
# Authority: dag

# ExcludeDist: el4

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name XML-NamespaceSupport

Summary: XML-NamespaceSupport Perl module
Name: perl-XML-NamespaceSupport
Version: 1.09
Release: 1.2
License: GPL or Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/XML-NamespaceSupport/

Source: http://www.cpan.org/modules/by-module/XML/XML-NamespaceSupport-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(ExtUtils::MakeMaker), perl

%description
XML-NamespaceSupport Perl module.

%prep
%setup -n %{real_name}-%{version}

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL \
	PREFIX="%{buildroot}%{_prefix}" \
	INSTALLDIRS="vendor"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
%{__rm} -rf %{buildroot}%{_libdir}/perl5/*/*-linux-thread-multi/
%{__rm} -f %{buildroot}%{_libdir}/perl5/vendor_perl/*/*-linux-thread-multi/auto/*{,/*}/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST README
%doc %{_mandir}/man?/*
%{perl_vendorlib}/XML/NamespaceSupport.pm

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.09-1.2
- Rebuild for Fedora Core 5.

* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 1.09-1
- Updated to release 1.09.

* Sun Aug 24 2003 Dag Wieers <dag@wieers.com> - 1.08-1
- Fixed site -> vendor. (Matthew Mastracci)

* Wed May 28 2003 Dag Wieers <dag@wieers.com> - 1.08-0
- Initial package. (using DAR)
