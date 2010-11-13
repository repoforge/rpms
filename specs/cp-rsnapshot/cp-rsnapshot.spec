# $Id$
# Authority: dries

Summary: GNU cp (coreutils) which uses less memory with -al (for rsnapshot)
Name: cp-rsnapshot
Version: 0.0.0
Release: 0.1%{?dist}
License: GPLv3+
Group: System Environment/Base
URL: http://savannah.gnu.org/projects/coreutils

Source: ftp://alpha.gnu.org/gnu/coreutils/coreutils-7.0.tar.gz
Patch0: cp-use-less-memory-coreutils-7.0.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
Rsnapshot uses 'cp -al' on directories which contain all your backups. This 
can be a lot of files and the current coreutils cp keeps unused data about 
each file in memory when used with the options '-al'. A patch applied by Jim 
Meyering on 19 Nov 2008 with headline 'cp: use far less memory in some cases'
fixes this. This makes it possible to use an old machine with big disks and 
limited memory as an rsnapshot backup server. This fix should be available in 
the version of coreutils which will be released after coreutils 7.0.

This cp command is made from an alpha version of coreutils with a patch i 
found in the git tree, so USE THIS AT YOUR OWN RISK.

If you want to use this with rsnapshot, then change the cmd_cp var in 
rsnapshot.conf to:
cmd_cp=/usr/bin/cp-rsnapshot

Details:
http://thread.gmane.org/gmane.comp.gnu.coreutils.bugs/15081
http://git.savannah.gnu.org/gitweb/?p=coreutils.git;a=commitdiff;h=3ece0355d52e41a1b079c0c46477a32250278c11

%prep
%setup -n coreutils-7.0
%patch0 -p1

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
#  {__make} install DESTDIR="%{buildroot}"
%{__install} -Dp -m0755 src/cp %{buildroot}%{_bindir}/cp-rsnapshot

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README THANKS TODO
%{_bindir}/cp-rsnapshot

%changelog
* Mon Jan  5 2009 Dries Verachtert <dries@ulyssis.org> - 0.0.0-0.1
- Initial package.
