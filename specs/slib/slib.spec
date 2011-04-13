# $Id$
# Authority: dag

### EL4 ships with umb-scheme-3.2-36.EL4
### EL3 ships with umb-scheme-3.2-31
### EL2 ships with umb-scheme-3.2-21
# ExcludeDist: el2 el3 el4

Summary: Platform independent library for scheme
Name: slib
Version: 3b2
Release: 1%{?dist}
License: SLIB
Group: Development/Languages
URL: http://swissnet.ai.mit.edu/~jaffer/SLIB.html

Source0: http://swiss.csail.mit.edu/ftpdir/scm/slib-%{version}.zip
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
Requires(post): /sbin/install-info
Requires(preun): /sbin/install-info

%description
"SLIB" is a portable library for the programming language Scheme.
It provides a platform independent framework for using "packages" of
Scheme procedures and syntax.  As distributed, SLIB contains useful
packages for all Scheme implementations.  Its catalog can be
transparently extended to accommodate packages specific to a site,
implementation, user, or directory.

%prep
%setup -n %{name}
%{__perl} -pi.orig -e "s|/usr/(local/)?lib/slib|%{_datadir}/slib|g" *.init

%build

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_datadir}/slib/
%{__cp} -av *.scm *.init *.xyz *.txt *.dat *.ps %{buildroot}%{_datadir}/slib/
%{__install} -Dp -m0644 slib.info %{buildroot}%{_infodir}/slib.info

%clean
%{__rm} -rf %{buildroot}

%post
/sbin/install-info %{_infodir}/slib.info.gz %{_infodir}/dir &>/dev/null || :

%preun
if (( $1 == 0 )); then
    /sbin/install-info --delete %{_infodir}/slib.info.gz %{_infodir}/dir &>/dev/null || :
fi

%files
%defattr(-, root, root, 0755)
%doc ANNOUNCE README COPYING FAQ ChangeLog
%doc %{_infodir}/slib.*
%{_datadir}/slib/

%changelog
* Thu Mar 24 2011 Dag Wieers <dag@wieers.com> - 3b2-1
- Initial package. (based on fedora)
