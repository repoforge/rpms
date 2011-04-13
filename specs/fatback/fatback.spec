# $Id$
# Authority: dag

Summary: Tool for recovering files from FAT file systems
Name: fatback
Version: 1.3
Release: 1%{?dist}
License: GPL
Group: Applications/File
URL: http://sourceforge.net/projects/fatback/

Source: http://dl.sf.net/project/fatback/fatback/fatback-%{version}/fatback-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: flex

%description
Fatback is a forensic tool for undeleting files from Microsoft FAT
file systems.  Fatback is different from other undelete tools in that
it does the following:

   * Runs under UNIX environments (only Linux and FreeBSD tested so far)
   * Can undelete files automatically
   * Supports Long File Names
   * Supports FAT12, FAT16, and FAT32
   * Powerful interactive mode
   * Recursively undeletes deleted directories
   * Recovers lost cluster chains
   * Works with single partitions or whole disks

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

### Clean up buildroot
%{__rm} -f %{buildroot}%{_infodir}/dir

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README 
%doc %{_infodir}/fatback-manual.info*
%doc %{_mandir}/man1/fatback.1*
%{_bindir}/fatback

%changelog
* Tue Feb 15 2011 Dag Wieers <dag@wieers.com> - 1.3-1
- Initial package. (using DAR)
