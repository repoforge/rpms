# $Id$
# Authority: dries
# Upstream: Hans Oesterholt-Dijkema <oesterhol$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Tie-Cache-LRU-Expires

Summary: Perl implementation of a least-recently used cache with expiration
Name: perl-Tie-Cache-LRU-Expires
Version: 0.54
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Tie-Cache-LRU-Expires/

Source: http://www.cpan.org/modules/by-module/Tie/Tie-Cache-LRU-Expires-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(Class::Virtual)
BuildRequires: perl(Tie::Cache::LRU)
BuildRequires: perl(ExtUtils::MakeMaker)

%description
A LRU cache is similar to the kind of cache used by a web browser. New items
are placed into the top of the cache. When the cache grows past its size limit,
it throws away items off the bottom. The trick is that whenever an item is
-accessed-, it is pulled back to the top. The end result of all this is that
items which are frequently accessed tend to stay in the cache.

This is an expiring LRU cache. Each entry in this cache expires after 'EXPIRES'
seconds (default 3600). The cache is in RAM (see Tie::Cache::LRU). ENTRIES
provides the maximum number of entries in the Tie::Cache::LRU cache.

It works by checking if a cached entry hasn't expired. If it has, undef is
returned, otherwise it's value. If the entry wasn't cached, undef is also
returned (of course). Expired entries will eventually drop of the LRU; or, if
referenced will (as can be expected, otherwise they wouldn't be referenced) be
refreshed.

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
%doc ChangeLog README
%doc %{_mandir}/man3/Tie::Cache::LRU::Expires*
%dir %{perl_vendorlib}/Tie
%dir %{perl_vendorlib}/Tie/Cache
%dir %{perl_vendorlib}/Tie/Cache/LRU
%{perl_vendorlib}/Tie/Cache/LRU/Expires.pm

%changelog
* Tue Jul 18 2006 Al Pacifico <adpacifico@users.sourceforge.net> - 0.54-1
- Initial packaging.
