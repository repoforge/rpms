# $Id$
# Authority: dag
# Upstream: Adam Spiers <adam$spiers,net>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name URI-Bookmarks

Summary: Perl module class encapsulating an entry in a typical bookmark file
Name: perl-URI-Bookmarks
Version: 0.92
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/URI-Bookmarks/

Source: http://www.cpan.org/modules/by-module/URI/URI-Bookmarks-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
perl-URI-Bookmarks is a Perl module class encapsulating an entry
in a typical bookmark file.

This package contains the following Perl module:

    URI::Bookmarks

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
%doc INSTALL MANIFEST README
%doc %{_mandir}/man3/URI::Bookmark.3pm*
%doc %{_mandir}/man3/URI::Bookmark::Netscape.3pm*
%doc %{_mandir}/man3/URI::Bookmarks.3pm*
%doc %{_mandir}/man3/URI::Bookmarks::Netscape.3pm*
%dir %{perl_vendorlib}/URI/
%{perl_vendorlib}/URI/Bookmark/
%{perl_vendorlib}/URI/Bookmark.pm
%{perl_vendorlib}/URI/Bookmarks/
%{perl_vendorlib}/URI/Bookmarks.pm
%dir %{perl_vendorlib}/auto/URI/
%{perl_vendorlib}/auto/URI/Bookmark/
%{perl_vendorlib}/auto/URI/Bookmarks/

%changelog
* Sun Nov 04 2007 Dag Wieers <dag@wieers.com> - 0.92-1
- Initial package. (using DAR)
