# $Id$
# Authority: dag

### EL6 ships with diffstat-1.51-2.el6
### EL5 ships with diffstat-1.41-1.2.3.el5
### EL4 ships with diffstat-1.31-5
### EL3 ships with diffstat-1.31-2
### EL2 ships with diffstat-1.28-1
# Tag: rfx

Summary: Tool to provide statistics based on the output of diff
Name: diffstat
Version: 1.53
Release: 1%{?dist}
License: MIT
Group: Development/Tools
URL: http://invisible-island.net/diffstat/

#Source0: http://invisible-island.net/datafiles/release/diffstat.tar.gz
Source0: http://invisible-island.net/datafiles/release/diffstat-%{version}.tar.gz
Source1: COPYING
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: xz

%description
The diff command compares files line by line.  Diffstat reads the
output of the diff command and displays a histogram of the insertions,
deletions and modifications in each file.  Diffstat is commonly used
to provide a summary of the changes in large, complex patch files.

Install diffstat if you need a program which provides a summary of the
diff command's output.

%prep
%setup
%{__cp} -v %{SOURCE1} .

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGES COPYING README
%doc %{_mandir}/*/*
%{_bindir}/diffstat

%changelog
* Tue Jul 20 2010 Dag Wieers <dag@wieers.com> - 1.53-1
- Initial package. (using DAR)
