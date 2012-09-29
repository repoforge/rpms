# $Id$
# Authority: dfateyev

### RHEL6 comes with 0.7.5-4
%{?el6:# Tag: rfx}

%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

Name: python-netaddr
Version: 0.7.10
Release: 1%{?dist}
Summary: A pure Python network address representation and manipulation library

Group: Development/Libraries
License: BSD
URL: http://github.com/drkjam/netaddr
Source0: http://github.com/downloads/drkjam/netaddr/netaddr-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: python-devel >= 2.4


%description
A pure Python network address representation and manipulation library.

netaddr provides a Pythonic way of working with :-

- IPv4 and IPv6 addresses and subnets
- MAC addresses, OUI and IAB identifiers, IEEE EUI-64 identifiers
- arbitrary (non-aligned) IP address ranges and IP address sets
- various non-CIDR IP range formats such as nmap and glob-style formats

Included are routines for :-

- generating, sorting and summarizing IP addresses and networks
- performing easy conversions between address notations and formats
- detecting, parsing and formatting network address representations
- performing set-based operations on groups of IP addresses and subnets
- working with arbitrary IP address ranges and formats
- accessing OUI and IAB organisational information published by IEEE
- accessing IP address and block information published by IANA

For details on the latest updates and changes, see :-

    http://github.com/drkjam/netaddr/blob/rel-0.7.x/CHANGELOG

API documentation for the latest release is available here :-

    http://packages.python.org/netaddr/


%prep
%setup -n netaddr-%{version}

# Make rpmlint happy, get rid of DOS line endings
%{__sed} -i 's/\r//' netaddr/*.py
%{__sed} -i 's/\r//' netaddr/ip/*.py
%{__sed} -i 's/\r//' netaddr/eui/*.idx

# Make rpmlint happy, rip out python shebang lines from most python
# modules
find netaddr -name "*.py" | \
  xargs %{__perl} -ni -e 'print unless /usr\/bin\/python|env\s+python/'


%build
%{__python} setup.py build


%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root %{buildroot}


%check
%{__python} netaddr/tests/__init__.py

%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc AUTHORS CHANGELOG COPYRIGHT INSTALL LICENSE PKG-INFO
%doc README docs/source/
%{python_sitelib}/*
%{_bindir}/netaddr

%changelog
* Sat Sep 29 2012 Denis Fateyev <denis@fateyev.com> - 0.7.10-1
- Update to 0.7.10
- Rebuild for Repoforge

* Tue Oct 05 2010 John Eckersberg <jeckersb@redhat.com> - 0.7.5-1
- New upstream release 0.7.5
- Updated summary and description to match upstream README
- Updated URL and source to reflect upstream move to github

* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 0.7.4-2
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Mon May 17 2010 John Eckersberg <jeckersb@redhat.com> - 0.7.4-1
- New upstream release 0.7.4

* Wed Sep 30 2009 John Eckersberg <jeckersb@redhat.com> - 0.7.3-1
- New upstream release 0.7.3

* Fri Aug 21 2009 John Eckersberg <jeckersb@redhat.com> - 0.7.2-1
- New upstream release 0.7.2
- Updated Summary and Description with new values provided by upstream

* Mon Aug 17 2009 John Eckersberg <jeckersb@redhat.com> - 0.7.1-1
- New upstream release 0.7.1 fixes naming conflict with 'nash' by
  renaming the netaddr shell to 'netaddr'

* Wed Aug 12 2009 John Eckersberg <jeckersb@redhat.com> - 0.7-1
- Upstream release 0.7

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jul 22 2009 John Eckersberg <jeckersb@redhat.com> - 0.6.3-2
- Minor tweaks to spec file aligning with latest Fedora packaging guidelines
- Enforce python 2.4 dependency as needed by netaddr >= 0.6.2
- Drop BR on python-setuptool as it is not imported in setup.py
- Drop BR on dos2unix use sed instead
- Align description with that of delivered PKG-INFO
- Rip out python shebangs
- Add %%check section to enable tests
- Thanks to Gareth Armstrong <gareth.armstrong@hp.com>

* Tue Jun 23 2009 John Eckersberg <jeckersb@redhat.com> - 0.6.3-1
- New upstream bugfix release

* Mon Apr 13 2009 John Eckersberg <jeckersb@redhat.com> - 0.6.2-1
- New upstream bugfix release

* Tue Apr 7 2009 John Eckersberg <jeckersb@redhat.com> - 0.6.1-1
- New upstream bugfix release

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Feb 18 2009 John Eckersberg <jeckersb@redhat.com> - 0.6-2
- Add BuildDepends on dos2unix to clean up some upstream sources

* Wed Feb 18 2009 John Eckersberg <jeckersb@redhat.com> - 0.6-1
- New upstream version

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 0.5.2-2
- Rebuild for Python 2.6

* Fri Oct 10 2008 John Eckersberg <jeckersb@redhat.com> - 0.5.2-1
- New upstream version, bug fixes for 0.5.1

* Tue Sep 23 2008 John Eckersberg <jeckersb@redhat.com> - 0.5.1-1
- New upstream version, bug fixes for 0.5

* Sun Sep 21 2008 John Eckersberg <jeckersb@redhat.com> - 0.5-1
- New upstream version

* Mon Aug 11 2008 John Eckersberg <jeckersb@redhat.com> - 0.4-1
- Initial packaging for Fedora

