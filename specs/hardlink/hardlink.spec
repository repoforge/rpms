# $Id$

# Authority: dag

Summary:  A utility to hardlink duplicate files in a directory tree.
Name: hardlink
Version: 1.2
Release: 1
License: GPL
Group: Applications/System
URL: ftp://ftp.redhat.com/pub/redhat/mirror-tools/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: ftp://ftp.redhat.com/pub/redhat/mirror-tools/hardlink.c
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

%description
A utility to hardlink duplicate files in a directory tree.

%prep
%setup -c -T
%{__cp} -af %{SOURCE0} .

%build
${CC:-%{__cc}} %{optflags} -o hardlink hardlink.c

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_bindir}
%{__install} -m0755 hardlink %{buildroot}%{_bindir}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%{_bindir}/*

%changelog
* Tue Apr 29 2003 Dag Wieers <dag@wieers.com> - 1.2-1
- Build happens in its own buildsubdir.

* Sun Apr 20 2003 Dag Wieers <dag@wieers.com> - 1.2-0
- Initial build. (using DAR)
