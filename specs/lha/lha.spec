# $Id$
# Authority: dag

# ExclusiveDist: el4,el5,el6

%define _default_patch_fuzz 2

Summary: Archiving and compression utility for LHarc format archives
Name: lha
Version: 1.14i
Release: 19.2.2%{?dist}
License: freeware
Group: Applications/Archiving
URL: http://www2m.biglobe.ne.jp/~dolphin/lha/prog/

Source: http://www2m.biglobe.ne.jp/~dolphin/lha/prog/lha-114i.tar.gz
Patch0: lha-114i-symlink.patch
Patch1: lha-114i-malloc.patch
Patch2: lha-114i-sec.patch
Patch3: lha-dir_length_bounds_check.patch
Patch4: lha-114i-sec2.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
LHA is an archiving and compression utility for LHarc format archives.
LHA is mostly used in the DOS world, but can be used under Linux to
extract DOS files from LHA archives.

Install the lha package if you need to extract DOS files from LHA archives.

%prep
%setup -n lha-114i

%patch0 -p1 -b .symlink
%patch1 -p1 -b .malloc

# security fixes
%patch2 -p1 -b .sec
%patch3 -p1 -b .sec
%patch4 -p1 -b .sec

%build
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 src/lha %{buildroot}%{_bindir}/lha
#%{__install} -Dp -m0644 man/lha.man %{buildroot}%{_mandir}/jp/man1/lha.1

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGES.euc MACHINES*.euc PROBLEMS.euc README.euc *.txt
#%doc %{_mandir}/jp/man1/lha.1*
%{_bindir}/lha

%changelog
* Sun Jan 15 2012 David Hrbáč <david@hrbac.cz> - 1.14i-19.2.2
- builds fine on el{4,5,6}

* Mon Apr 30 2007 Dag Wieers <dag@wieers.com> - 1.14i-19.2.2
- Import from RHEL.
